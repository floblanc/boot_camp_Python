def ft_filter(function_to_apply, list_of_inputs):
	return (i for i in list_of_inputs if function_to_apply(i))