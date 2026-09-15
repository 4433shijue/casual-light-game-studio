export const level = Object.freeze({ goal: 5, seconds: 20, positions: [[160,180],[470,300],[300,210],[150,320],[480,170]] });
export class Round {
  constructor() { this.reset(); }
  reset() { this.score = 0; this.remaining = level.seconds; this.state = 'playing'; }
  togglePause() { if (this.state === 'playing') this.state = 'paused'; else if (this.state === 'paused') this.state = 'playing'; }
  tick(seconds) {
    if (this.state !== 'playing' || !Number.isFinite(seconds) || seconds < 0) return;
    this.remaining = Math.max(0, this.remaining - seconds);
    if (this.remaining === 0) this.state = 'failed';
  }
  hit() { if (this.state === 'playing' && ++this.score >= level.goal) this.state = 'success'; }
}
