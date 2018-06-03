# Glossary of Theoretical Terms

All definitions and section/page numbers are taken from:

_Information Flow: The Logic of Distributed Systems_. Jon Barwise and Jerry Seligman. Cambridge University Press, 1997.


## Classification
###### (Section 2.1, Page 28)
###### (Section 4.1, Page 69)

A _classification_ `A := < tok(A), typ(A), |=  >` consists of:

- A set `tok(A)` of objects called _tokens_;
- A set `typ(A)` of objects called _types_;
- A binary relation `|=` of _validity_ on `tok(A) X typ(A)`;

The relation `x |= alpha` reads _x has type alpha_ or _alpha is valid for x_. The inverse relation `x |!= alpha` reads _x does not have type alpha_ or _alpha is invalid for x_.


## Infomorphism
###### (Section 2.1, Page 32)
###### (Section 4.2, Page 72)

Given two [classifications](#classification):

- `A := < tok(A), typ(A), |=_A >`
- `C := < tok(C), typ(C), |=_C >`

an _infomorphism_ between `A` and `C` is a pair of functions `f := < f_up, f_down >` satisfying:

- `f_up : typ(A) -> typ(C)`
- `f_down : typ(C) -> typ(A)`

and the _Fundamental Infomorphism Axiom_: for all `c in tok(C)` and `alpha in typ(A)`:

```
f_down(c) |=_A alpha  <if and only if>  c |=_C f_up(alpha)
```
Here, an infomorphism between `A` and `C` is denoted `A <--> C`.


## Channel
###### (Section 4.3, Page 76)

A _channel_ is a set of [infomorphisms](#infomorphism) `{f_i : A_i <--> C}` that all share a common codomain `C`. The [classification](#classification) `C` is the _core_ of the channel.


## Sum
###### (Section 5.1, Page 81)

Given two [classifications](#classification) `A` and `B`, the sum `A + B` is the classification such that:

- `tok(A + B)` is the Cartesian product `tok(A) X tok(B)`;
- `typ(A + B)` is the disjoint union of:
  - `{(0, alpha) for alpha in typ(A)}`
  - `{(1, beta) for beta in typ(B)}`.
- The validity relation `|=_[A+B]` is given by:

```
(a,b) |=_[A+B] (0,alpha)  <if and only if>  a |=_A alpha
(a,b) |=_[A+B] (1,beta)   <if and only if>  b |=_B beta
```

## Invariant
###### (Section 5.2, Page 84)

### By Type

Given a [classification](#classification) `A`, an _invariant_ `I := < Sigma, ~ >` consists of a subset of `typ(A)`, denoted `Sigma`, and a binary relation `~` on `tok(A)` defined by:

```
a ~ b  <implies>  <for all> alpha in Sigma, a |= alpha  <if and only if>  b |= alpha
```
That is, `a ~ b` if and only if `a` and `b` agree on all types in `Sigma`.

### By Token (Dual)
###### (Section 5.2, Page 87)

Given a [classification](#classification) `A`, the _dual invariant_ `J := <Sigma, ~>` consists of a subset of `tok(A)`, denoted `Sigma`, and a binary relation `~` on `typ(A)` defined by:

```
alpha ~ beta  <implies>  <for all>  a in Sigma, a |= alpha  <if and only if> a |= beta
```
That is, `alpha ~ beta` if and only if `alpha` and `beta` are valid on exactly the same tokens in `Sigma`.

## Quotient
###### (Section 5.2, Page 84)

### By Type Invariant

Given a [classification](#classification) `A` and an [invariant](#invariant) `I := < Sigma, ~ >`, the _quotient_ of `A` by `I`, denoted `A/I`, is the classification given by:

- `typ(A/I)` is `Sigma`;
- `tok(A/I)` is the set of equivalence classes of `~`;
- `[a] |=_[A/I] alpha` if and only if `a |=_[A] alpha`, where `[a]` is the equivalence class of `a` under `~`.

### By Token Invariant (Dual)
###### (Section 5.2, Page 87)

Given a [classification](#classification) `A` and a [dual (token) invariant](#invariant) `J := < Sigma, ~ >`, the _dual quotient_ of `A` by `J`, denoted `A/J` is the classification given by:

- `typ(A/J)` is the set of equivalence classes under `~`;
- `tok(A/J)` is `Sigma`;
- `a |=_[A/J] [alpha]` if and only if `a |=_[A] alpha`, where `[alpha]` is the equivalence class of `alpha` under `~`.

More concisely, `A/I` (or `A/J`) is the classification obtained by restricting the types to `Sigma` and grouping together tokens by `~`. As the name suggests, taking a non-trivial quotient generally results in a smaller classification.
