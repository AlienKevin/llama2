samples = [
(
"let List.cons: (Int, [Int]) -> [Int] = fun x, xs -> ?? in test List.cons(1, []) == [1] end",
"let List.cons: (Int, [Int]) -> [Int] = fun x, xs -> x::xs in test List.cons(1, []) == [1] end",
),

("""
let List.length: [Int] -> Int = fun xs -> ?? in test List.length([1, 2]) == 2 end
""",
"""
let List.length: [Int] -> Int =
  fun xs ->
    case xs
      | [] => 0
      | _::xs => 1 + List.length(xs) end in test List.length([1, 2]) == 2 end
"""
),

("""
let List.hd: [Int] -> Int = fun l -> ?? in test List.hd([1, 2]) == 1 end
""",
"""
let List.hd: [Int] -> Int =
  fun l ->
    case l
      | [] => -1
      | x::xs => x end in test List.hd([1, 2]) == 1 end
"""
),

("""
let List.tl: [Int] -> [Int] = fun l -> ?? in test List.tl([1, 2]) == 2 end
""",
"""
let List.tl: [Int] -> [Int] =
  fun l ->
    case l
      | [] => []
      | x::xs => xs end in test List.tl([1, 2]) == 2 end
"""),

("""
let List.is_empty: [Int] -> Bool = fun xs -> ?? in test List.is_empty([]) == true end
""",
"""
let List.is_empty: [Int] -> Bool =
  fun xs ->
    case xs
      | [] => true
      | _::_ => false end in test List.is_empty([]) == true end
"""
),

("""
let List.nth: ([Int], Int) -> Int = fun xs, n -> ?? in
test List.nth([7, 8, 9], 2) == 9 end
""",
"""
let List.nth: ([Int], Int) -> Int =
  fun xs, n ->
    case xs, n
      | x::_, 0 => x
      | _::xs, n => List.nth(xs, n - 1)
      | [], _ => ? end in
test List.nth([7, 8, 9], 2) == 9 end
"""
),

("""
let List.rev: [Int] -> [Int] = fun l -> ?? in test List.rev([1, 2, 3]) == [3, 2, 1] end
""",
"""
let List.rev: [Int] -> [Int] =
fun l -> 
let go: ([Int], [Int]) -> [Int] =
  fun xs, acc -> 
    case xs 
      | [] => acc 
      | x::xs => go(xs, x::acc) end in
go(l, []) in test List.rev([1, 2, 3]) == [3, 2, 1] end
"""
),

("""
let List.equal: ((Int, Int) -> Bool, [Int], [Int]) -> Bool = fun p, xs, ys -> ?? in
test List.equal(fun a, b -> a == b, [1, 2, 3], [1, 2, 3]) end
""",
"""
let List.equal: ((Int, Int) -> Bool, [Int], [Int]) -> Bool =
fun p, xs, ys ->
case xs, ys
  | [], [] => true
  | x::xs, y::ys => p(x, y) && List.equal(p, xs, ys)
  | _ => false end in
test List.equal(fun a, b -> a == b, [1, 2, 3], [1, 2, 3]) end
"""),

("""
let List.init: (Int, Int -> Int) -> [Int] = fun len, f -> ?? in
test List.equal(fun a, b -> a == b, List.init(3, fun idx -> idx), [0, 1, 2]) end
""",
"""
let List.init: (Int, Int -> Int) -> [Int] =
fun len, f ->
let go: (Int, [Int]) -> [Int] =
fun idx, xs ->
  if idx < len 
    then go(idx + 1, xs @ [f(idx)])   
      else xs in
        go(0, []) in
test List.equal(fun a, b -> a == b, List.init(3, fun idx -> idx), [0, 1, 2]) end
"""
),

("""
let List.fold_left: ((Int, Int) -> Int, Int, [Int]) -> Int = ?? in
test List.fold_left(fun x, acc -> x + acc, 0, [1, 2, 3]) == 6 end
""",
"""
let List.fold_left: ((Int, Int) -> Int, Int, [Int]) -> Int =
  fun f, acc, xs ->
    case xs 
      | [] => acc
      | hd::tl => List.fold_left(f, f(acc, hd), tl) end in
test List.fold_left(fun x, acc -> x + acc, 0, [1, 2, 3]) == 6 end
"""),

("""
let List.fold_right: ((Int, Int) -> Int, [Int], Int) -> Int = fun f, xs, acc -> ?? in
test List.fold_right(fun (x, acc) -> x + acc, 0, [1, 2, 3]) == 6 end
""",
"""
let List.fold_right: ((Int, Int)-> Int, [Int], Int)-> Int =
  fun f, xs, acc ->
    case xs
      | [] => acc
      | hd::tl => f(hd, List.fold_right(f, tl, acc)) end in
test List.fold_right(fun (x, acc) -> x + acc, 0, [1, 2, 3]) == 6 end
""")
]

queries = [
"let List.filter: (Int -> Bool, [Int]) -> [Int] = fun p, xs -> ?? in test List.equal(fun a, b -> a == b, List.filter(fun x -> x != 2, [1, 2, 3]), [1, 3]) end",
"let List.append: (([Int], [Int]) -> [Int]) = fun xs, ys -> ?? in test List.equal(fun a, b -> a == b, List.append([1, 2], [3, 4]), [1, 2, 3, 4]) end",
"let List.mapi: ((Int, Int) -> Int, [Int]) -> [Int] = fun f, xs -> ?? in test List.equal(fun a, b -> a == b, List.mapi(fun i, x -> i * x, [1, 2, 3]), [0, 2, 6]) end",
"let List.find: (Int -> Bool, [Int]) -> OptionInt = fun p, xs -> ?? in test OptionInt.equal(List.find(fun x -> x == 2, [0, 1, 2]), Some(2)) end",
"let List.filter_map: (Int -> ?, [Int]) -> [Int] = fun p, xs -> ?? in test List.equal(fun a, b -> a == b, List.filter_map(fun x -> if x == 2 then ? else x + 1, [1, 2, 3]), [2, 4]) end",
"""\
# An Expression is a variable, function, or application #
type Exp =
  + Var(String)
  + Lam(String, Exp)
  + Ap(Exp, Exp) in
# Syntatic Equality of Expressions #
let exp_equal: (Exp, Exp) -> Bool =
  fun es -> ??
in
test exp_equal(Ap(Lam("x", Var("x")), Var("y")), Ap(Lam("x", Var("x")), Var("y"))) end""",
"""\
# Substitute Exp v for variable name in Exp e #
let subst: (Exp, String, Exp) -> Exp=
  fun v, name, e ->
  ??
in
test exp_equal(subst(Var("z"), "y", Ap(Lam("x", Var("x")), Var("y"))), Ap(Lam("x", Var("x")), Var("z"))) end;""",
"""\
# Evaluation can result in either an Exp or an Error #
type Result =
  + Error(String)
  + Ok(Exp) 
in
let result_equal: (Result, Result) -> Bool =
fun rs ->
  case rs
    | Ok(e1), Ok(e2) => exp_equal(e1, e2)
    | Error(e1), Error(e2) => e1 $== e2
    | _ => false
  end
in

# Evaluation by substitution #
let eval: Exp -> Result =
  fun e ->
    ??
in
test result_equal(
  eval(Var("yo")),
  Error("Free Variable")) end;

test result_equal(
  eval(Ap(Var("no"), Lam("bro", Var("bro")))),
  Error("Not a Function")) end;

test result_equal(
  eval(Lam("yo", Var("yo"))),
  Ok(Lam("yo", Var("yo")))) end;

test result_equal(
  eval(Ap(Lam("yo", Var("yo")), Lam("bro", Var("bro")))),
  Ok(Lam("bro", Var("bro")))) end
"""
]
