formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("One", "Two", "Three", "Four"))
print(formatter % (True, False, True, False))
print("%r %r %r %r %r %r %r %r" % (
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight.",
	"I had this thing.",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight."
	)
)
