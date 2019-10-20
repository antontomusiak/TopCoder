class ProgressBar:
	def showProgress(self, taskTimes, tasksCompleted):
		total_time = float(sum(taskTimes))
		time_completed = float(sum(taskTimes[:tasksCompleted]))
		p_completed = int(20 * time_completed / total_time)
		progress_bar = '#' * p_completed + '.' * (20 - p_completed)
		return progress_bar