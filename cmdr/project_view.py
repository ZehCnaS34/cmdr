ID = 1

class ProjectView:
    def __init__(self, project):
        self.model = project

    def list_jobs(self):
        global ID
        ID += 1
        return '\n'.join(self.model.jobs.keys())

    def render(self):
        return self.list_jobs()
