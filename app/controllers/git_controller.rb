class GitController < ApplicationController
  def index
    @tagline = 'in-dev-forever'
    @command_name = %x(python python/generate_info.py git_command)
    @command_desc = 'does things'
    @version_num = '2.1.0'
  end
end
