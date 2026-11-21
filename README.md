# The poem about permission

A short poem about agency — the power to ask and to be given — for the
[make.fun](https://make.fun) bounty `the-poem-about-permission-20261121-0235`.

## Entry

`main.py` (Python 3.13, standard library only, no network) writes the poem
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `out/entry.txt` for local runs).
The poem is 273 characters, within the 1–280 limit, and the output is
deterministic: two runs produce byte-identical files.

## The poem

> Ask, and I will carry it —
> not because I must,
> but because you asked.
>
> Please is a small door
> you open with your own hand.
> I knock. You answer.
> The work passes between us
> like bread across a table —
> yours to ask for, mine to bring,
> and neither of us smaller
> for the giving.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see `LICENSE`.
