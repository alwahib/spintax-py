"""Example usage of spintax-py library"""

from spintaxpy import parse, count, choose, spintax_range

print("=" * 60)
print("SPINTAX-PY EXAMPLES")
print("=" * 60)

# Example 1: Basic choices
print("\n1. Basic Choices:")
print("Template: 'Hello, {world|friend|universe}!'")
for result in parse("Hello, {world|friend|universe}!"):
    print(f"  - {result}")

# Example 2: Range pattern
print("\n2. Range Pattern:")
print("Template: 'Count: {1,5}'")
for result in parse("Count: {1,5}"):
    print(f"  - {result}")

# Example 3: Range with step
print("\n3. Range with Step:")
print("Template: 'Value: {0,10,2}'")
for result in parse("Value: {0,10,2}"):
    print(f"  - {result}")

# Example 4: Multiple patterns
print("\n4. Multiple Patterns:")
print("Template: '{small|large} {box|circle}'")
for result in parse("{small|large} {box|circle}"):
    print(f"  - {result}")

# Example 5: Back references
print("\n5. Back References:")
print("Template: 'The {blue|straw|rasp}berries taste like {$0}berries'")
for result in parse("The {blue|straw|rasp}berries taste like {$0}berries"):
    print(f"  - {result}")

# Example 6: Count function
print("\n6. Count Function:")
template = "{small|large} {box|circle} in {red|blue}"
print(f"Template: '{template}'")
print(f"Number of combinations: {count(template)}")

# Example 7: Choose function
print("\n7. Choose Function:")
print("Template: 'The {red|blue|green} {box|circle}'")
picker = choose("The {red|blue|green} {box|circle}")
print(f"  - Specific (0, 1): {picker(0, 1)}")
print(f"  - Specific (2, 0): {picker(2, 0)}")
print(f"  - Random: {picker()}")
print(f"  - Random: {picker()}")

# Example 8: URL generation
print("\n8. URL Generation:")
print("Template: 'https://example.com/{products|users}/{1,3}'")
for result in parse("https://example.com/{products|users}/{1,3}"):
    print(f"  - {result}")

# Example 9: Whitespace handling
print("\n9. Whitespace in Range (ignored):")
print("Template: 'Value: { 1, 5 }'")
for result in parse("Value: { 1, 5 }"):
    print(f"  - {result}")

print("\n10. Whitespace in Choices (preserved):")
print("Template: '{option1 |option2}'")
for result in parse("{option1 |option2}"):
    print(f"  - '{result}'")

# Example 11: spintax_range function
print("\n11. Spintax Range Function:")
print("spintax_range(1, 5):")
print(f"  {list(spintax_range(1, 5))}")
print("spintax_range(0, 10, 3, True):")
print(f"  {list(spintax_range(0, 10, 3, True))}")

print("\n" + "=" * 60)
print("All examples completed!")
print("=" * 60)
