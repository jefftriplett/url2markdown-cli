from invoke import run, task


@task
def git_push():
    run('git push origin --all')
    run('git push github --all')


@task
def pypi():
    run('python setup.py sdist')
    run('python setup.py bdist_wheel')


@task
def pypi_upload():
    run('python setup.py sdist upload')
    run('python setup.py bdist_wheel upload')
