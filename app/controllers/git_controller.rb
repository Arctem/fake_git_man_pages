class GitController < ApplicationController
  def index
    @tagline = 'test'
    @command_name = 'status'
    @command_desc = 'does things'
    @version_num = '2.1.0'
  end
end
