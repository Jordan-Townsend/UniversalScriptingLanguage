"""Fresh bounded .usl discovery and transfer through the15 new native profiles.
Run against extracted v4.10 source. This does not learn language grammars.
"""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import argparse,ast,hashlib,json,sys,tempfile,time

def transfer(request):
 from usl_systems.semantic_next_functions import NextFunctionFrontend,source_for
 from usl_systems.entity_program_discovery import ProgramDiscovery
 from usl_systems.intent_contracts import prove_expression
 language,expression,source,contract,cases=request
 proof=prove_expression(expression,contract);assert proof['proved']
 rows=[{'arguments':[c['input']],'expected_result':int(c['expected_stdout']),'intent':c['oracle']['source']} for c in cases]
 f=NextFunctionFrontend(language,source_for(language,expression),'transform',contract,rows)
 checks=[f.verify(target) for target in ('python','javascript')]
 original=[]
 for c in cases:
  observed=ProgramDiscovery._execute(source,c['input'],'int','int')
  original.append({'input':c['input'],'independent_expected':c['expected_stdout'],'observed':observed,'passed':observed['stdout']==c['expected_stdout']})
 return {'catalog_id':language,'actual_learned_USL_source':source,'learned_source_model_intent':proof,'native_source':f.source,
 'fresh_original_USL_checks':original,'native_and_generated_checks':checks,'passed':all(c['passed'] for c in original) and all(c['passed'] for c in checks),
 'fresh_native_program_executions':sum(c['native_executions'] for c in checks),'native_observations_replayed':0}

def main():
 p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output',type=Path,default=Path('learned_native_transfer.json'));p.add_argument('--workers',type=int,default=4);p.add_argument('--i-allow-execution',action='store_true');a=p.parse_args()
 if not a.i_allow_execution:raise ValueError('Explicit trusted fixture/native execution required')
 if not 1<=a.workers<=16:raise ValueError('Worker count must be1..16')
 root=a.source_root.resolve();sys.path.insert(0,str(root))
 from usl_systems.entity_program_discovery import ProgramDiscovery,DiscoverySession
 from usl_systems.semantic_next_functions import LANGUAGES,NextFunctionFrontend,source_for
 from usl_systems.language import Interpreter,parse
 from usl_systems.intent_contracts import prove_expression
 from usl_systems.resources import discover
 from usl_systems.batch_multiplex import source_identity
 from usl_systems.entity_memory import fingerprint
 identity=source_identity();started=time.monotonic();oracle={'source':'Independently authored2x+1 training, new protected holdout and separate new-language transfer intent'}
 def cases(table):return [{'input':n,'expected_stdout':str(v)+'\n','oracle':oracle} for n,v in table]
 data={'protected':{'schema':'usl.discovery.protected-suite.v1','name':'learned_affine','input_type':'int','output_type':'int','holdout':cases([(-17,-33),(23,47)]),'retention':[]},
 'discovery':{'schema':'usl.discovery.request.v1','name':'learned_affine','input_type':'int','output_type':'int','hypothesis':'Infer bounded integer affine behaviour from three independent examples.','evidence':oracle,'grammar':{'schema':'usl.discovery.typed-grammar.v1','constants':[0,1,2],'operators':['+','*'],'expression_depth':2,'expression_limit':128},'training':cases([(-3,-5),(0,1),(4,9)]),'max_candidates':4096,'max_seconds':20}}
 study='let sealed = seal_discovery_suite(artifact("protected"))\nlet learned = discover_program(artifact("discovery"), sealed["suite_id"])\nassert learned["promoted"]\nprint("new bounded USL skill promoted after sealed holdout")\n'
 contract={'schema':'usl.intent.integer.v1','inputs':{'value':{'min':-1000,'max':1000}},'postcondition':'result == value*2+1'}
 independent=cases([(-31,-61),(19,39),(77,155)])
 workers=min(a.workers,max(1,int(discover()['cpu_effective'])),len(LANGUAGES))
 with tempfile.TemporaryDirectory(prefix='usl-v410-fresh-study-') as directory:
  discovery=ProgramDiscovery(directory);observed_study=DiscoverySession(discovery,data,approved=True).interpret(study)
  skill=discovery.memory.skill('learned_affine');doc=skill['document'];assert fingerprint(doc)==skill['sha256']
  tree=parse(doc['source']);assert len(tree.body)==3 and isinstance(tree.body[0],ast.Assign) and tree.body[0].targets[0].id=='value' and isinstance(tree.body[0].value,ast.Call) and tree.body[0].value.func.id=='input_value'
  assert isinstance(tree.body[1],ast.Assign) and tree.body[1].targets[0].id=='result' and isinstance(tree.body[2],ast.Expr) and isinstance(tree.body[2].value,ast.Call) and tree.body[2].value.func.id=='print' and len(tree.body[2].value.args)==1 and isinstance(tree.body[2].value.args[0],ast.Name) and tree.body[2].value.args[0].id=='result'
  expression=ast.unparse(tree.body[1].value);assert prove_expression(expression,contract)['proved']
  selected=discovery.memory.run(doc['discovery_run_id'])['document'];checks=[]
  def multiplex(ids):
   if ids!=sorted(LANGUAGES):raise ValueError('Every exact new native profile must retain independent transfer')
   requests=[(n,expression,doc['source'],contract,independent) for n in ids]
   with ProcessPoolExecutor(max_workers=workers) as pool:checks.extend(pool.map(transfer,requests))
   return {'passed':all(r['passed'] for r in checks),'count':len(checks),'native_programs':sum(r['fresh_native_program_executions'] for r in checks)}
  supervisor='let ids = new_native_ids()\nlet result = multiplex_learned_transfer(ids)\nassert result["passed"]\nassert result["count"] == 15\nprint("actual new native learned transfers", result["count"])\nprint("fresh native programs", result["native_programs"])\n'
  observed=Interpreter(capabilities={'new_native_ids':lambda:sorted(LANGUAGES),'multiplex_learned_transfer':multiplex},timeout=3600).run(supervisor)
  try:NextFunctionFrontend('wast',source_for('wast',expression),'transform',{**contract,'postcondition':'result ==91'},[{'arguments':[-31],'expected_result':-61,'intent':oracle['source']}]);wrong=False
  except ValueError:wrong=True
  preserved=discovery.memory.skill('learned_affine')['sha256']==skill['sha256'];assert wrong and preserved
  report={'schema':'usl.new-native.learned-transfer.v1','passed':all(r['passed'] for r in checks) and wrong and preserved,'profile_ids':sorted(LANGUAGES),'profile_count':len(checks),
   'fresh_discovery_USL_supervisor':{'source':study,'observed':observed_study},'actual_discovered_skill':skill,'discovery_record':selected,'complete_candidate_trials':discovery.history(doc['discovery_run_id']),
   'native_transfer_USL_supervisor':{'source':supervisor,'stdout':observed.output,'operations':observed.operations},'transfers':checks,'fresh_native_program_executions':sum(r['fresh_native_program_executions'] for r in checks),
   'original_learned_USL_executions':3*len(checks),'generated_USL_executions':2*len(checks),'wrong_intent_rejected_before_native_program_execution':wrong,'active_skill_preserved':preserved,
   'protected_holdout_is_new_and_one_use':True,'retention_suite_empty':True,'workers':workers,'elapsed_seconds':time.monotonic()-started,'source_identity':identity,'source_unchanged_during_run':source_identity()==identity,
   'native_observations_replayed':0,'formal_scope':'All-domain bounded int32 primitive arithmetic for this learned task; native compiler/runtime trust boundaries remain unqualified',
   'language_grammars_learned':False,'general_self_study_or_human_equivalence':False,'complete_entity_tracks':0,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['passed','profile_count','fresh_native_program_executions','workers','elapsed_seconds','source_unchanged_during_run','language_grammars_learned']}))
 if not report['passed']:raise SystemExit(1)
if __name__=='__main__':main()
