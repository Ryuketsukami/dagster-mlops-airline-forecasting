Here is where we can replicate our production env locally for development, and then reproduce these systems for testing purposes.
here ewe can define external api/services tools and storage/db locations
"if you can access in python, you can make a resource out of it"

instead of hard coding db connections, api clients or filepaths, we inject them as dependencies
our asset declares what it needs, like a db connection or storage client, and dagster provides those from outside the function

its good for encapsulation, our data just does processing