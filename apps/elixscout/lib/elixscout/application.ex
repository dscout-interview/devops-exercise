defmodule Elixscout.Application do
  use Application

  def start(_type, _args) do
    children = [
      {Bandit, plug: Elixscout.Router, port: 4000}
    ]

    Supervisor.start_link(children, strategy: :one_for_one, name: Elixscout.Supervisor)
  end
end
