from django.db import models
from django.contrib.auth.models import User



class Problem(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	input_format = models.TextField()
	output_format = models.TextField()
	sample_input = models.TextField()
	sample_output = models.TextField()
	time_limit = models.FloatField(default=1.0)  # Time limit for code execution in seconds




class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="Pending")  # Status of submission (e.g., Accepted, Wrong Answer, Runtime Error)

    def __str__(self):
        return f"{self.user.username}'s submission for {self.problem.title}"