SHELL=/bin/bash
PYTHON=python3
PYTHON_ENV=env

DATABASE=lona_project/db.sqlite3

HOST=0.0.0.0
PORT=8080
LOG_LEVEL=info
SHELL_SERVER_URL=file://socket

.PHONY: clean freeze shell server shell-server

# environment #################################################################
$(PYTHON_ENV)/.created: REQUIREMENTS.txt
	rm -rf $(PYTHON_DEV) && \
	$(PYTHON) -m venv $(PYTHON_ENV) && \
	. $(PYTHON_ENV)/bin/activate && \
	pip install pip --upgrade && \
	pip install -r ./REQUIREMENTS.txt && \
	date > $(PYTHON_ENV)/.created

env: $(PYTHON_ENV)/.created

clean:
	rm -rf $(PYTHON_ENV)
	rm -rf $(DATABASE)
	rm -rf lona_project/static/upload/*

freeze: env
	. $(PYTHON_ENV)/bin/activate && \
	pip freeze

shell: env
	. $(PYTHON_ENV)/bin/activate && \
	rlpython

# database ####################################################################
$(DATABASE): env
	. $(PYTHON_ENV)/bin/activate && \
	./lona_project/manage.py migrate

db: $(DATABASE)

super-user: env $(DATABASE)
	. $(PYTHON_ENV)/bin/activate && \
	./lona_project/manage.py createsuperuser

# lona ########################################################################
server: env
	. $(PYTHON_ENV)/bin/activate && \
	lona run-server \
		--project-root=lona_project \
		-s settings.py \
		--host $(HOST) \
		--port $(PORT) \
		--log-level=$(LOG_LEVEL) \
		--shell-server-url=$(SHELL_SERVER_URL) \
		$(args)

server-shell: env
	. $(PYTHON_ENV)/bin/activate && \
	rlpython $(SHELL_SERVER_URL) $(args)
