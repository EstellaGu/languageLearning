import sys
import random

kana = {
	'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
	'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
	'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
	'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
	'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
	'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
	'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
	'や': 'ya', 'ゆ': 'yu', 'よ': 'yo', 
	'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
	'わ': 'wa'
}

katakana = {
	'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
	'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
	'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
	'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
	'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
	'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
	'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
	'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo', 
	'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
	'ワ': 'wa'
}

voicedKana = {
	'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
	'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
	'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
	'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
	'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po'
}

voicedKatakana = {
	'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',
	'ザ': 'za', 'ジ': 'zi', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',
	'ダ': 'da', 'ヂ': 'ji', 'ヅ': 'zu', 'デ': 'de', 'ド': 'do',
	'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
	'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po'
}

difficultKana = {
	'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
	'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
	'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
	'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo', 
	'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
	'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo', 
	'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
	'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo', 
	'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo', 
	'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
	'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo'
}

difficultKatakana = {
	'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
	'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
	'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
	'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo', 
	'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
	'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo', 
	'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
	'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo', 
	'ジャ': 'ja', 'ジュ': 'ju', 'ジョ':  'jo', 
	'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
	'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}


def test(dict, keyMeaning, valueMeaning):
	print("随时可以输入back重新选择测试类型")
	nextToDo = ''
	while True:
		if nextToDo == 'exit' or nextToDo == 'back':
			break

		type = random.randint(0, 1)
		key = random.choice(list(dict.keys()))
		value = dict[key]
		if type == 0:
			print("请写出以下%s对应的%s，并按回车键查看答案" % (valueMeaning, keyMeaning))
			nextToDo = input(value)
			if nextToDo != 'exit' and nextToDo != 'back':
				print(key)
				nextToDo = input("按回车键继续\n")
		elif type == 1:
			print("请输入以下%s对应的%s，并按回车键查看答案" % (keyMeaning, valueMeaning))
			print(key)
			nextToDo = input()
			if nextToDo == value:
				print("答对了")
				nextToDo = input("按回车键继续")
				print()
			elif nextToDo != 'exit' and nextToDo != 'back':
				print("答错了，正确答案是%s" % (value))
				nextToDo = input("按回车键继续")
				print()
		else:
			print("Unreachable")

	if nextToDo == 'back':
		chooseTest()
	elif nextToDo == 'exit':
		exit()
	else:
		print("Unreachable")


def chooseTest():
	testChoices = ['五十音平假名', '五十音片假名', '浊音平假名', '浊音片假名', '拗音平假名', '拗音片假名', '混合测试']
	print("请选择测试内容：")
	for index, item in enumerate(testChoices):
		print("%s(%d)" % (item, index + 1))

	while True:
		choice = input()

		if choice == 'exit': 
			exit()

		try:
			choice = int(choice)
			if choice not in range(1, len(testChoices) + 1):
				print("请输入1~%d之间的数字" % (len(testChoices)))
			else:
				break
		except:
			print("请输入1~%d之间的数字" % (len(testChoices)))

	if choice == 1:
		test(kana, '平假名', '读音')
	elif choice == 2:
		test(katakana, '片假名', '读音')
	elif choice == 3:
		test(voicedKana, '浊音平假名', '读音')
	elif choice == 4:
		test(voicedKatakana, '浊音片假名', '读音')
	elif choice == 5:
		test(difficultKana, '拗音平假名', '读音')
	elif choice == 6:
		test(difficultKatakana, '拗音片假名', '读音')
	elif choice == 7:
		test({**kana, **katakana, **voicedKana, **voicedKatakana, **difficultKana, **difficultKatakana}, '字符', '读音')
	else:
		print("Unreachable")


def exit():
	try:
		sys.exit(0)
	finally:
		print("后会有期")

 
print("随时可以输入exit退出程序")
chooseTest()





