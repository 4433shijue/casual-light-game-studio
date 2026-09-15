extends SceneTree

func _initialize() -> void:
	var model = load("res://round.gd").new()
	model.toggle_pause()
	model.tick(100)
	model.hit()
	assert(model.score == 0 and model.remaining == 20)
	model.toggle_pause()
	for i in range(5):
		model.hit()
	model.tick(100)
	model.hit()
	assert(model.state == "success" and model.score == 5)
	for i in range(3):
		model.reset()
		assert(model.score == 0 and model.remaining == 20 and model.state == "playing")
		model.tick(21)
		model.hit()
		assert(model.state == "failed" and model.score == 0)
	print("Round smoke passed")
	quit()
