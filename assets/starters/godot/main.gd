extends Control

const RoundModel = preload("res://round.gd")
const POINTS = [Vector2(130, 150), Vector2(440, 260), Vector2(270, 190), Vector2(130, 260), Vector2(450, 140)]
var round_model = RoundModel.new()
var best: int = 0
var hud: Label
var message: Label
var target: Button
var pause_button: Button

func _ready() -> void:
	var config = ConfigFile.new()
	if config.load("user://casual-click-v1.cfg") == OK:
		var value = config.get_value("score", "best", 0)
		if value is int and value >= 0 and value <= RoundModel.GOAL:
			best = value
	make_label("点点原型", 15)
	hud = make_label("", 65)
	message = make_label("", 350)
	target = make_button("点击", Vector2(130, 150), Vector2(70, 70), on_hit)
	pause_button = make_button("暂停", Vector2(120, 410), Vector2(165, 45), on_pause)
	make_button("重新开始", Vector2(355, 410), Vector2(165, 45), on_restart)
	refresh()

func make_label(text: String, y: float) -> Label:
	var label = Label.new()
	label.text = text
	label.position = Vector2(0, y)
	label.size = Vector2(640, 45)
	label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	label.add_theme_font_size_override("font_size", 22)
	add_child(label)
	return label

func make_button(text: String, pos: Vector2, dimensions: Vector2, action: Callable) -> Button:
	var button = Button.new()
	button.text = text
	button.position = pos
	button.size = dimensions
	button.pressed.connect(action)
	add_child(button)
	return button

func _process(delta: float) -> void:
	round_model.tick(delta)
	refresh()

func on_hit() -> void:
	round_model.hit()
	if round_model.score > best:
		best = round_model.score
		var config = ConfigFile.new()
		config.set_value("score", "best", best)
		var error = config.save("user://casual-click-v1.cfg")
		if error != OK:
			push_warning("成绩未保存，本轮可继续游玩")
	refresh()

func on_pause() -> void:
	round_model.toggle_pause()
	refresh()

func on_restart() -> void:
	round_model.reset()
	refresh()

func refresh() -> void:
	hud.text = "目标 %d/%d   剩余 %d 秒   最佳 %d" % [round_model.score, RoundModel.GOAL, ceili(round_model.remaining), best]
	target.visible = round_model.state == "playing"
	target.position = POINTS[round_model.score % POINTS.size()]
	pause_button.text = "继续" if round_model.state == "paused" else "暂停"
	message.text = {"playing": "点击目标，达到分数即可过关", "paused": "已暂停", "success": "完成！可以重新开始", "failed": "时间到，再试一次"}[round_model.state]
