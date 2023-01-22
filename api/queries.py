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

MUTATION_USER = gql(
    """
    mutation createUserMutation($input: UserCreateInput!) {
        user(data: $input ) {
            email
            id
            password
            username
        }
    }
    """)

MUTATION_FILE_UPLOAD = gql(
    """
    mutation ReadFileMutation($filename: String!, $file: Upload!) {
        readFile(filename: $filename, file: $file){
            filename
        }
    }
    """)
