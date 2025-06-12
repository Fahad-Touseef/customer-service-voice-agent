.PHONY: sync
sync:
	cd frontend && npm install
	cd server && uv sync


.PHONY: serve
serve:
	cd frontend && npm run dev

