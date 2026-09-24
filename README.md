# DevOps Exercise

A small monorepo with two apps, each with a couple of tests.

- `apps/pyscout` - tiny Flask app (Python). `/login` calls elixscout for auth.
- `apps/elixscout` - tiny Elixir/Plug/Bandit HTTP service. `/auth/ping` returns `{"authenticated": true}`.

Set `ELIXSCOUT_URL` to point pyscout at a running elixscout (defaults to `http://localhost:4000`).
