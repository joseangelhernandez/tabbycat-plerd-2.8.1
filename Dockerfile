FROM python:3.9

# Just needed for all things python (note this is setting an env variable)
ENV PYTHONUNBUFFERED 1
# Needed for correct settings input
ENV IN_DOCKER 1

# Setup Node/NPM
RUN apt-get update
RUN apt-get install -y curl nginx
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

# Copy all our files into the baseimage and cd to that directory
RUN mkdir /tcd
WORKDIR /tcd
ADD . /tcd/

# Set git to use HTTPS (SSH is often blocked by firewalls)
RUN git config --global url."https://".insteadOf git://

# Install our node/python requirements
RUN pip install pipenv
RUN pipenv install --system --deploy
RUN npm ci --only=production

# Compile all the static files
RUN npm run build
RUN python ./tabbycat/manage.py collectstatic --noinput -v 0

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "tabbycat.wsgi:application"]
