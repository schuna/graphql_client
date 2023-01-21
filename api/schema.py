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

QUERY_USER = gql(
    """
    query UserQuery($user_id: Int!) {
        user(userId: $user_id) {
            email
            id
            password
            username
        }
    }
    """)
