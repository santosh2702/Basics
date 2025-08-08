
### 🧠 Variable Scope, Keywords, and Behavior

1. **What is the output if a local variable has the same name as a class member?**

   * The local variable shadows the class member within its scope.

2. **Can a `ref` parameter be used with a constant?**

   * ❌ No, constants are immutable.

3. **What happens if you pass a variable marked `readonly` to a method with `ref`?**

   * ❌ Compilation error. `readonly` fields can't be passed by `ref`.

4. **Can you declare a variable using `var` without assigning a value?**

   * ❌ No. Type inference requires an initializer.

5. **What happens if a method returns a reference to a local variable?**

   * ❌ Compile-time error. Local variables cannot be returned by reference.

6. **Can you have multiple `static` constructors in a class?**

   * ❌ No. Only one static constructor is allowed per class.

7. **What happens if you throw `null` in C#? (`throw null;`)**

   * ❌ `NullReferenceException` at runtime.

8. **Can a class be both `abstract` and `sealed`?**

   * ❌ No. They are mutually exclusive.

9. **Can `const` fields be assigned from another `const` field?**

   * ✅ Yes, as long as the other `const` is accessible and already resolved at compile time.

10. **What’s the default value of a static reference field if not initialized?**

    * `null`

---

### 🔄 Control Flow and Loop Traps

11. **What happens when you use `break` inside a `finally` block?**

    * ❌ Compilation error. Control cannot leave the `finally` block using `break`.

12. **What is the output of a `while` loop with no increment and no condition break?**

    * Infinite loop. May cause application to hang or crash.

13. **Can you use `goto` to jump into a loop?**

    * ❌ No. `goto` cannot enter a block that requires initialization like loops.

14. **What happens when you use `continue` inside a `switch` within a loop?**

    * ❌ Compilation error unless inside a loop.

15. **Can a `switch` statement be used on a `null` string?**

    * ❌ `NullReferenceException` at runtime unless null is handled explicitly.

---

### 🔒 Exception Handling

16. **Can you have a `try` block without any `catch`, only `finally`?**

    * ✅ Yes. It is legal.

17. **Will `finally` block run if there's a `return` statement in `try`?**

    * ✅ Yes. `finally` always runs.

18. **Can `throw` be used without any exception object?**

    * ✅ Yes, only inside `catch` to rethrow the same exception.

19. **Will the code in `finally` execute if `Environment.Exit()` is called?**

    * ❌ No. Application terminates immediately.

20. **What happens if an exception is thrown inside a `finally` block?**

    * The exception overrides any exception from the `try` or `catch` blocks.

---

### 🧵 Multithreading and Tasks

21. **What happens if two threads update the same `List<T>`?**

    * Undefined behavior, possible `InvalidOperationException`. Not thread-safe.

22. **Is `Task.Run()` the same as creating a new thread?**

    * ❌ No. It's part of the thread pool. More efficient but pooled.

23. **What’s the output when awaiting a completed Task?**

    * Returns immediately.

24. **What happens if you don’t `await` an async method?**

    * It runs but the caller doesn’t wait for it to complete. Can cause race conditions.

25. **Can you `await` inside a `lock` statement?**

    * ❌ No. It causes deadlocks. Compilation error.

26. **Is `List<T>` thread-safe by default?**

    * ❌ No.

27. **What happens if you `await` inside a loop without capturing state?**

    * Common mistake leads to all tasks using final value of loop variable.

28. **Does `async void` return a Task?**

    * ❌ No. Returns nothing. Used for event handlers only.

29. **What’s the difference between `Thread.Abort()` and `Thread.Interrupt()`?**

    * `Abort` stops thread forcefully; `Interrupt` only interrupts if blocked.

30. **Can `Thread.Sleep()` be used in `async` methods?**

    * ✅ But it blocks the thread. Prefer `await Task.Delay()`.

---

### 🔗 Object Behavior and Memory

31. **What is the size of an empty class?**

    * 1 byte (minimum memory footprint to ensure object identity).

32. **Do two objects with same values point to the same memory?**

    * ❌ No. Unless interning is involved.

33. **Can two reference variables refer to the same object?**

    * ✅ Yes.

34. **Does string interning happen for all strings?**

    * ❌ Only for literals and manually interned strings.

35. **Can two boxed integers with the same value compare equal using `==`?**

    * ❌ No. They are different objects in memory.

---

### 📦 Boxing, Unboxing, and Types

36. **What happens when you box a value type and then change the original?**

    * Boxed copy remains unchanged.

37. **Can you unbox a value into the wrong type?**

    * ❌ InvalidCastException

38. **Is `null` a valid value for all reference types?**

    * ✅ Yes.

39. **What’s the difference between `is` and `as`?**

    * `is` checks type, `as` attempts cast and returns null if fails.

40. **Can `dynamic` bypass compile-time errors?**

    * ✅ Yes, errors occur at runtime.

---

### 🧰 Language Features and Misconceptions

41. **Can a method have two `params` arguments?**

    * ❌ No. Only one `params` parameter is allowed and it must be last.

42. **What’s the behavior of `??` with non-nullable types?**

    * `??` can't be used unless LHS is nullable.

43. **Can a `record` be mutable?**

    * ✅ Yes, with `record class` and `init`/`set` properties.

44. **Can you use LINQ `Where()` on `null`?**

    * ❌ NullReferenceException unless you null-check.

45. **What is the use of `nameof()` and when does it fail?**

    * Gets symbol name. Fails if used on non-symbol expressions.

46. **What is the difference between `default(T)` and `Activator.CreateInstance<T>()`?**

    * `default(T)` gives zero/null; `Activator` invokes constructor.

47. **What happens when you call `.ToString()` on `null`?**

    * ❌ NullReferenceException

48. **What is the output of `new object() == new object()`?**

    * `false` — different references.

49. **Can `readonly struct` contain mutable fields?**

    * ❌ No. It defeats purpose of `readonly`.

50. **Is `decimal` more precise than `double`?**

    * ✅ Yes, especially for financial calculations.

51. **Can a property setter be `private` and getter be `public`?**

    * ✅ Yes.

52. **Can `static` methods be overridden?**

    * ❌ No. Only instance methods can be overridden.

53. **What happens when you override `Equals()` without overriding `GetHashCode()`?**

    * May cause inconsistent behavior in collections.

54. **What does `null == null` return?**

    * `true`

55. **Can struct contain a parameterless constructor?**

    * ✅ Since C# 10.0, yes (with some limitations).
