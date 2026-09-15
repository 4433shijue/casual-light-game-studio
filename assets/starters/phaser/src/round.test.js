import { test } from 'node:test';
import assert from 'node:assert/strict';
import { Round, level } from './round.js';
test('pause freezes time and scoring; resume finishes; terminal state ignores input', () => {
  const round = new Round(); round.togglePause(); round.tick(100); round.hit();
  assert.equal(round.remaining, level.seconds); assert.equal(round.score, 0);
  round.togglePause(); for (let i=0;i<level.goal;i++) round.hit();
  round.tick(100); round.hit(); assert.equal(round.state, 'success'); assert.equal(round.score, level.goal);
});
test('timeout and repeated restart restore all round state', () => {
  const round = new Round();
  for (let i=0;i<3;i++) { round.hit(); round.tick(100); round.hit(); assert.equal(round.state,'failed'); assert.equal(round.score,1); round.reset(); assert.equal(round.score,0); assert.equal(round.remaining,level.seconds); assert.equal(round.state,'playing'); }
});
