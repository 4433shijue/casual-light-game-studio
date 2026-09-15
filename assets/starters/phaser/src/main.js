import { Round, level } from './round.js';
const Phaser = window.Phaser;
if (!Phaser) throw new Error('请先 npm install，并通过本地 HTTP 服务打开游戏');
class Play extends Phaser.Scene {
  create() {
    this.round = new Round(); this.best = 0;
    try { const n=Number(localStorage.getItem('casual-click-best-v1')); if(Number.isInteger(n)&&n>=0&&n<=level.goal) this.best=n; } catch {}
    this.add.text(320,30,'点点原型',{fontSize:'30px',color:'#ffffff'}).setOrigin(.5);
    this.hud=this.add.text(320,75,'',{fontSize:'20px',color:'#b9cddd'}).setOrigin(.5);
    this.target=this.add.circle(160,180,35,0x72ddbc).setInteractive({useHandCursor:true});
    this.target.on('pointerdown',()=>{ this.round.hit(); this.refresh(); });
    this.message=this.add.text(320,365,'',{fontSize:'20px',color:'#ffffff'}).setOrigin(.5);
    this.pause=this.button(210,425,'暂停',()=>{this.round.togglePause();this.refresh();});
    this.button(430,425,'重新开始',()=>{this.round.reset();this.refresh();});
    this.refresh();
  }
  button(x,y,text,action) {
    const bg=this.add.rectangle(x,y,165,45,0x304a66).setInteractive({useHandCursor:true});
    const label=this.add.text(x,y,text,{fontSize:'20px',color:'#ffffff'}).setOrigin(.5);
    bg.on('pointerdown',action); return label;
  }
  update(_time,delta) { this.round.tick(delta/1000); this.refresh(); }
  refresh() {
    const r=this.round;
    if(r.score>this.best){this.best=r.score;try{localStorage.setItem('casual-click-best-v1',String(this.best));}catch{}}
    this.hud.setText(`目标 ${r.score}/${level.goal}   剩余 ${Math.ceil(r.remaining)} 秒   最佳 ${this.best}`);
    this.target.setVisible(r.state==='playing');
    const p=level.positions[r.score%level.positions.length]; this.target.setPosition(...p);
    this.pause.setText(r.state==='paused'?'继续':'暂停');
    this.message.setText({playing:'点击绿色圆点，达到目标即可过关',paused:'已暂停',success:'完成！可以重新开始',failed:'时间到，再试一次'}[r.state]);
  }
}
new Phaser.Game({type:Phaser.AUTO,parent:'game',width:640,height:480,backgroundColor:'#142132',scale:{mode:Phaser.Scale.FIT,autoCenter:Phaser.Scale.CENTER_BOTH},scene:Play});
