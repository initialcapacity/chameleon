# Chameleon

Simply import and instantiate Chameleon and call any method you want.
Chameleon implements the method so you don't have to! 

```python
from chameleon import Chameleon

chameleon = Chameleon()

print(chameleon.add(4, 3))
print(chameleon.multiply(4, 3))
print(chameleon.fibonacci(20))
print(chameleon.nth_prime(400))
print(chameleon.list_github_repositories(organization="initialcapacity"))
print(chameleon.search_the_web(search_term="pickles"))
chameleon.print_an_ascii_art_dinosaur_thats_saying_this_phrase(phrase="I'm artificially intelligent")
print(chameleon.solve_integral(function_string="x^2 * sin(x)", start="0", end="π"))
```

![chameleon logo](./readme-images/chameleon.png)
