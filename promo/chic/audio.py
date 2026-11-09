import asyncio, edge_tts, numpy as np, wave, subprocess, pathlib, sys
H=pathlib.Path(__file__).parent; A=H/'audio'; A.mkdir(exist_ok=True)
V="ko-KR-InJoonNeural"
L=[("v1","연말정산, 또 토해낼 거예요?",0.2,"+36%"),
   ("v2","바꿀 수 있는 것만.",3.35,"+10%"),
   ("v3","결제수단 하나만 바꿔도, 세금이 줄어요.",5.7,"+20%"),
   ("v4","덜 내는 건 십이월까지. 베타 신청하기.",10.4,"+28%")]
async def main():
    for n,t,_,r in L: await edge_tts.Communicate(t,V,rate=r,pitch="-6Hz").save(str(A/f'{n}.mp3'))
asyncio.run(main())
for n,*_ in L:
    d=subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(A/f'{n}.mp3')]).decode().strip()
    print(n,d)
# music
sr=44100; T=15; N=sr*T; x=np.zeros(N)
bpm=100; beat=60/bpm
def add(sig,t0,g=1):
    i=int(t0*sr); j=min(N,i+len(sig)); x[i:j]+=sig[:j-i]*g
tk=np.arange(int(.35*sr))/sr
kick=np.sin(2*np.pi*(55+90*np.exp(-tk*30))*tk)*np.exp(-tk*9)
rng=np.random.default_rng(1)
hat=(rng.standard_normal(int(.06*sr)))*np.exp(-np.arange(int(.06*sr))/sr*80); hat=np.diff(hat,prepend=0)
tb=np.arange(int(beat*2*sr))/sr
bass=lambda f:np.sin(2*np.pi*f*tb)*np.exp(-tb*1.6)
t=0.0;k=0
while t<T-.1:
    if t>=3.0 or t<2.9:
        if t>=3.0 or (k%2==0):
            add(kick,t,.9 if t>=3 else .5)
    add(hat,t+beat/2,.18 if t>=3 else .08)
    if k%8==0: add(bass(55),t,.45)
    if k%8==4: add(bass(49),t,.45)
    t+=beat;k+=1
# riser into 3.0, and a hit at 10.3
tr=np.arange(int(2.7*sr))/sr; ris=np.diff(rng.standard_normal(len(tr)),prepend=0)*(tr/2.7)**2*.12; add(ris,.3)
th=np.arange(int(1.5*sr))/sr; add(np.sin(2*np.pi*40*th)*np.exp(-th*3)*1.0,10.3)
# pad
tp=np.arange(N)/sr; pad=sum(np.sin(2*np.pi*f*tp) for f in (110,164.8,220,261.6))*.05*np.clip(tp/3,0,1)
x+=pad
x=np.tanh(x*1.2); x/= np.abs(x).max(); x*=.8
with wave.open(str(A/'music.wav'),'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x*32767).astype(np.int16).tobytes())
