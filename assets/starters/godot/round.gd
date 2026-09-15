extends RefCounted

const GOAL: int = 5
const SECONDS: float = 20.0
var score: int = 0
var remaining: float = SECONDS
var state: String = "playing"

func reset() -> void:
	score = 0
	remaining = SECONDS
	state = "playing"

func tick(delta: float) -> void:
	if state != "playing" or not is_finite(delta) or delta < 0:
		return
	remaining = maxf(0, remaining - delta)
	if remaining == 0:
		state = "failed"

func hit() -> void:
	if state == "playing":
		score += 1
		if score >= GOAL:
			state = "success"

func toggle_pause() -> void:
	if state == "playing":
		state = "paused"
	elif state == "paused":
		state = "playing"
