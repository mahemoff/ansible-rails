# ansible-rails

Ansible library to work with bundler and rails related commands.

## example: rake command

**available options**

    - path:
      description:
        - path which should cd'd into to run commands
      required: yes
    - command:
      description:
        - an arbitrary rake command to be executed
      required: yes
      default: no
    - executable:
      description:
        - Bundler executable
      required: no
      default: $GEM_HOME/bin/bundle
    - rails_env:
      description:
        - RAILS_ENV used by commands
      required: no
    - bundled:
      description:
        - use `bundle exec rake` or `bundle exec rails` instead of `rake` and `rails`
      required: no
      default: no
    - force:
      description:
        - force command in question
      required: no
      default: no

**examples**

    # run rake db:migrate
    rake: path=/path rails_env=staging command="db:migrate"

    # run rake db:migrate only of /current/db/schema.rb and /next/db/schema.rb are different
    rake:
      path: "/path"
      rails_env: "staging"
      command: "db:migrate"
      diff_paths:
        - { current: '/current/db/schema.rb', next: '/next/db/schema.rb' }

    # run bundle exec rake db:migrate
    rake: path=/path rails_env=staging command="db:migrate" bundled=yes

    # run bundle exec rake assets:precompile
    rake: path=/path rails_env=staging command="assets:precompile" bundled=yes

    # run bundle exec rake my:custom:command
    rake: path=/path rails_env=staging bundled=yes command="my:custom:command"

See [ansible-rails-deployment][1] for more usage examples.

### Tests

To execute tests for the `rake` command run the following in the project directory:

    PYTHONPATH=$PWD/library python test/rake_test.py

## example: bundle command

**available options**

    - executable:
      description:
        - Bundler executable
      required: no
      default: $GEM_HOME/bin/bundle
    - deployment:
      description:
        - Run for deployment
      required: false
      default: yes
    - binstubs:
      description:
        - generate binstubs
      required: false
      default: no
    - gemfile:
      description:
        - Path of Gemfile to run against
      required: false
      default: yes
    - path:
      description:
        - Path to install dependencies into
      required: false

**examples**

    # install a specific Gemfile to `shared/vendor`
    bundle: path=shared/vendor gemfile=/path/to/gemfile

    # install with option --deployment
    bundle: path=shared/vendor deployment=yes

    # use a specific bundler binary
    bundle: path=shared/vendor executable=$HOME/.rvm/wrappers/bundle


### Tests

To execute tests for the `bundle` command run the following in the project directory:

    PYTHONPATH=$PWD/library python test/bundle_test.py

[1]:https://github.com/nicolai86/ansible-rails-deployment