def WebIDLTest(parser, harness):
    threw = False
    try:
        parser.parse("""
            interface NullableUndefined {
              undefined? foo();
            };
        """)

        results = parser.finish()
    except:
        threw = True

    harness.ok(threw, "Should have thrown.")