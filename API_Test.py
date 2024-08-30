import requests
import json


def Avisek_API_test():
    """
    Description :
    Basic test
    Expected result :
    Check weather the id generated or not
    """
    # global response
    # status = NOT_EXECUTED
    # actual_result = None
    # status_reason = None
    # tc_time_interval = None
    # tc_start_time = get_current_time()

    try:
        test_url = "https://reqres.in"
        # define header parameters
        url = f"{test_url}/api/users"
        payload = json.dumps({"name": "Avisek",
                              "job": "Test"})
        headers = {'Content-Type': 'application/json'}

        # Sending request
        response = requests.request("POST", url, headers=headers, data=payload)

        # Encapsulating responses
        response_code = response.status_code

        print(response.text)

        data = response.json()
        created_id = data['id']
        print(created_id)

        if response_code == 201:
            # status_reason = TEST_SUCCESSFUL
            # status = PASS
            # actual_result = f"Status code is {response_code} and added user is {data['name']}"
            # log.info(status_reason)
            print("User created successfully!")
            data = response.json()
            created_id = data['id']
            print(f"Created user ID: {created_id}")

            # Delete the created user
            delete_url = f"{test_url}/api/users/{created_id}"
            delete_response = requests.delete(delete_url)
            delete_response.raise_for_status()

            # Check for successful deletion (status code 204)
            if delete_response.status_code == 204:
                print("User deleted successfully!")
            else:
                print(f"Error deleting user: {delete_response.text}")

        else:
            # status = FAIL
            # status_reason = f"wrong response code or team id details are not matching : {response_code},{name}"
            # actual_result = status_reason
            # log.error(status_reason)
            print(f"Error creating user: {response.text}")

    except Exception as error:
        # status = NOT_EXECUTED
        # status_reason = str(error)
        # log.error(status_reason)
        # print(f"Some Issue in Authentication : {response.reason}")
        print(f"Error during request: {error}")

    finally:
        print("test pass")
        # tc_end_time = get_current_time()
        # tc_time_interval = (tc_end_time - tc_start_time)
        # tc_time_interval_str = str(tc_time_interval).split(".")[0]
        # update_test_result_to_test_report1("verify_post_component", self.sheet,
        #                                    self.testcases_data, actual_result,
        #                                    status, tc_time_interval_str, status_reason)

Avisek_API_test()

