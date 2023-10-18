import functools
import os

import nox

nox.options.envdir = "build/nox"

@nox.session(python="3.8")
def docs(session):
    """Build the documentation."""
    output_dir = os.path.abspath(os.path.join(session.create_tmp(), "output"))
    doctrees, html = map(
        functools.partial(os.path.join, output_dir), ["doctrees", "html"]
    )
    print(html)
    session.run("rm", "-rf", output_dir, external=True)
    session.install("-r", "requirements.txt")
    session.cd("doc")
    sphinx_cmd = "sphinx-build"
    session.run(sphinx_cmd, "-b", "html", "-W", "-d", doctrees, ".", html)
