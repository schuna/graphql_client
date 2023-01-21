from gql import gql

QUERY_USERS = gql(
    """
    query {
        users {
            email
            id
            password
            username
        }
    }
    """)
