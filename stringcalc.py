def string_cal(str_num):
	if str_num == "":
		return "0"
	elif len(str_num) > 1:
		temp = 0
		for ch in str_num:
			if ch == "-":
				# print("negative", ch)
				return "negatives not allowed -" + str_num[str_num.index(ch) + 1]
		for ch in str_num:

			if (ch.isdigit()):
				temp = temp + int(ch)
		return temp

	else:
		return int(str_num)
