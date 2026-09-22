# Flask / FastAPI Backend Exercises

Based on the "improve existing backend" test format you're likely to get (Flask/FastAPI, API design, DB, Agile/Scrum shop). Set up a small starter API (one or two SQLAlchemy models, a couple of routes) and use it as the base for all of these — that's the most realistic way to train for a take-home test on an existing codebase.

---

## 🟢 Beginner (1–10)

**1. Add a missing endpoint**
Add a `PATCH /items/{id}` endpoint that partially updates a resource (only fields provided in the body are changed).

**2. Correct status codes**
Audit an existing set of routes and fix status codes: `201` on create, `204` on delete (no body), `404` when not found, `422` on validation error.

**3. Add pagination**
Add `?page=` and `?limit=` query params to a list endpoint that currently returns everything. Return the total count alongside the page.

**4. Add basic filtering**
Add `?status=` and `?category=` query params to filter a list endpoint, without string-interpolating values into SQL.

**5. Add sorting**
Add a `?sort=` query param (e.g. `sort=price` or `sort=-price` for descending) to a list endpoint.

**6. Input validation with Pydantic / Marshmallow**
Take a route that reads raw `request.json` / dict input and replace it with a proper Pydantic model (FastAPI) or Marshmallow schema (Flask), rejecting bad payloads with a clear 422.

**7. Consistent error responses**
Replace ad-hoc `return {"error": ...}, 400` calls scattered across routes with one consistent error response shape and a global exception handler.

**8. Health check endpoint**
Add a `GET /health` endpoint that checks the app is up and the DB connection works, returning `200` or `503`.

**9. Environment-based config**
Refactor hardcoded config (DB URL, secret key) into environment variables with sensible defaults for local dev.

**10. Write your first tests**
Using `pytest` + `TestClient` (FastAPI) or the Flask test client, write tests for one endpoint: happy path, 404 case, and validation error case.

---

## 🟡 Medium (11–20)

**11. Fix an N+1 query**
Given a route that loops over parent objects and queries their children individually, rewrite it using a join or `selectinload`/`joinedload` to do it in one query.

**12. Move logic out of the route**
Take a "fat" route that mixes request parsing, business logic, and DB access, and refactor it into a service/repository layer, keeping the route thin.

**13. Add JWT authentication**
Add login (`POST /auth/login`) issuing a JWT, and protect a route so it requires a valid token via a dependency (FastAPI) or decorator (Flask).

**14. Add role-based access**
Extend the auth above so some routes require an `admin` role, returning `403` for authenticated-but-unauthorized users.

**15. Nested resource endpoint**
Add `GET /users/{id}/orders` returning only that user's related resources, with a 404 if the user doesn't exist.

**16. Database migration**
Add a new column to a model (e.g. `created_at`) and write the Alembic migration for it, without dropping existing data.

**17. Business rule / constraint**
Add a rule like "a room can't be double-booked for overlapping time slots" — enforce it at the application level and explain how you'd also enforce it at the DB level.

**18. Reproduce and fix a planted bug**
Take an off-by-one bug in a pagination implementation (e.g. `offset = page * limit` vs `(page - 1) * limit`) and fix it with a test that would have caught it.

**19. Idempotent endpoint**
Make a `POST /orders` endpoint safe to retry (e.g. via an `Idempotency-Key` header) so a network retry doesn't create a duplicate order.

**20. Dockerize it**
Write a `Dockerfile` and `docker-compose.yml` that runs the API plus a Postgres container, with the API waiting for the DB to be ready.

---

## 🔴 Advanced (21–29 + bonus)

**21. Async trap**
Given a FastAPI route declared `async def` that calls a blocking DB driver or `time.sleep`, explain why this blocks the event loop for all requests, and fix it (sync route, `run_in_threadpool`, or an async driver).

**22. Rate limiting middleware**
Implement basic rate limiting (sliding window or token bucket) as middleware, limiting each client to N requests per minute.

**23. Background task**
Move a slow operation (e.g. sending a confirmation email) out of the request/response cycle using FastAPI `BackgroundTasks` or a Celery task, so the API responds immediately.

**24. Caching a hot endpoint**
Add caching (in-memory or Redis) to an expensive read-heavy endpoint, with a sensible invalidation strategy when the underlying data changes.

**25. Interval overlap detection**
Given a list of booking intervals `[(start, end), ...]`, write a function that detects whether a new interval overlaps any existing one — then wire it into the booking endpoint from #17.

**26. Build a nested category tree**
Given a flat table of categories with `parent_id`, write an endpoint that returns them as a nested JSON tree, and detect cycles if a category is ever mis-parented to a descendant.

**27. Aggregation endpoint**
Given raw order rows, add an endpoint returning totals grouped by month and category (via the ORM's `group_by`, not Python loops).

**28. Transactions and rollback**
Write an endpoint that performs two related writes (e.g. debit one account, credit another) inside a single transaction, and prove that a failure in the second write rolls back the first.

**29. Concurrency-safe counter**
Add a `POST /items/{id}/reserve` endpoint that decrements stock, and make it safe against two simultaneous requests over-reserving the same item (row locking or an atomic `UPDATE ... WHERE stock > 0`).

---

## Bonus — likely verbal/discussion questions (30–33)

**30.** Explain the app factory pattern in Flask (`create_app()`) — why use it instead of a global `app` object?

**31.** What is dependency injection in FastAPI (`Depends`), and how would you use it to share a DB session across routes?

**32.** Pydantic v1 vs v2 — what changed in validators and `.dict()`/`.model_dump()`, and why does it matter if the codebase mixes both?

**33.** When would you reach for Celery/RQ instead of `BackgroundTasks`, and when would you reach for Redis caching instead of just optimizing the query?

---

Say the word if you want `correction_flask.md` with worked solutions for these.