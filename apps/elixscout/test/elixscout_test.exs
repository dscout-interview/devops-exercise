defmodule ElixscoutTest do
  use ExUnit.Case

  test "hello" do
    assert Elixscout.hello() == "Hello, dscout!"
  end

  test "health" do
    assert Elixscout.health() == %{status: "ok"}
  end
end
