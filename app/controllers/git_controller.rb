class GitController < ApplicationController
  def index
    @tagline = 'test'
    @command_name = 'status'
    @command_desc = 'does things'
  end
end
