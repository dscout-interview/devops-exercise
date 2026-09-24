defmodule Elixscout.Router do
  use Plug.Router

  plug(:match)
  plug(:dispatch)

  get "/auth/ping" do
    send_resp(conn, 200, ~s({"authenticated": true}))
  end

  match _ do
    send_resp(conn, 404, "not found")
  end
end
