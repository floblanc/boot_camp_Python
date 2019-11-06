def ft_reduce(function_to_apply, list_of_inputs):
	res = list_of_inputs[0]
	for i in list_of_inputs:
		if i != list_of_inputs[0]:
			res = function_to_apply(res, i)
	return (res)