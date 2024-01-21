# appy
Albert Heijn Graphql Python API

API for the Albert Heijn GraphQL API

Thanks to [this gist from jabbink](https://gist.github.com/jabbink/8bfa44bdfc535d696b340c46d228fdd1) for information about authentication. The way to get the authorization code used in the authorize function is to go to https://login.ah.nl/secure/oauth/authorize?client_id=appie&redirect_uri=appie://login-exit&response_type=code and open the browser inspector network tab. Login with you credentials and the network inspector should show a failed request. The url of this failed request contains the code you will need.

This API makes use of the Albert Heijn GraphQL API at https://api.ah.nl/graphql
Using the GraphQL introspection the complete set of queries and mutations were extracted. You can check it for yourself at something like [GraphQL Voiager](https://graphql-kit.com/graphql-voyager/) using the introspection json.

<details>
  <summary>Visualization of the whole API:</summary>
     ![](/docs/albert_heijn_graphql.svg)
</details>


It's not ready for real use, but is used to test the queries and mutations as a proof of concept. 