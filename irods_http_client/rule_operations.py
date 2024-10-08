import requests
import json

class Rules:
    
    def __init__(self, url_base: str):
        """" 
        Initializes Rules with a base url. 
        Token is set to None initially, and updated when setToken() is called in irodsClient.
        """
        self.url_base = url_base
        self.token = None


    def list_rule_engines(self):
        """
        Lists available rule engine plugin instances.

        Returns
        - A dict containing the HTTP status code and iRODS response.
        - The iRODS response is only valid if no error occurred during HTTP communication.
        """
        
        headers = {
            'Authorization': 'Bearer ' + self.token,
        }

        params = {
            'op': 'list_rule_engines'
        }

        r = requests.get(self.url_base + '/rules', params=params, headers=headers)

        rdict = r.json()

        if (r.status_code / 100 == 2):
            if rdict['irods_response']['status_code']:
                print('Failed to retrieve rule engines list: iRODS Status Code' + str(rdict['irods_response']['status_code']))
            else:
                print('Rule engine list retrieved successfully')
            
            return(
                {
                    'status_code': r.status_code,
                    'data': rdict
                }
            )
        else:
            irods_err = ''
            rdict = None
            if (r.text != ''):
                rdict = r.json()
                irods_err = ': iRods Status Code' + str(rdict['irods_response'])
            print(f'Error <{r.status_code}>{irods_err}')

            return(
                {
                    'status_code': r.status_code,
                    'data': rdict
                }
            )


    def execute(self, rule_text: str, rep_instance: str=''):
        """
        Executes rule code.
        
        Parameters
        - rule_text: The rule code to execute.
        - rep_instance (optional): The rule engine plugin to run the rule-text against.

        Returns
        - A dict containing the HTTP status code and iRODS response.
        - The iRODS response is only valid if no error occurred during HTTP communication.
        """
        if (self.token == None):
            raise RuntimeError('No token set. Use setToken() to set the auth token to be used')
        if (not isinstance(rule_text, str)):
            raise TypeError('name must be a string')
        if (not isinstance(rep_instance, str)):
            raise TypeError('name must be a string')

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'op': 'execute',
            'rule-text': rule_text
        }

        if (rep_instance != ''):
            data['rep-instance'] = rep_instance

        r = requests.post(self.url_base + '/rules', headers=headers, data=data)

        if (r.status_code / 100 == 2):
            rdict = r.json()

            if rdict['irods_response']['status_code']:
                print('Failed to remove execute rule: iRODS Status Code' + str(rdict['irods_response']['status_code']))
            else:
                print('Rule executed successfully')
            
            return(
                {
                    'status_code': r.status_code,
                    'data': rdict
                }
            )
        else:
            irods_err = ''
            rdict = None
            if (r.text != ''):
                rdict = r.json()
                irods_err = ': iRods Status Code' + str(rdict['irods_response'])
            print(f'Error <{r.status_code}>{irods_err}')

            return(
                {
                    'status_code': r.status_code,
                    'data': rdict
                }
            )
        

    def remove_delay_rule(self, rule_id: int):
        """
        Removes a delay rule from the catalog.
        
        Parameters
        - rule_id: The id of the delay rule to be removed.

        Returns
        - A dict containing the HTTP status code and iRODS response.
        - The iRODS response is only valid if no error occurred during HTTP communication.
        """
        if (self.token == None):
            raise RuntimeError('No token set. Use setToken() to set the auth token to be used')
        if (not isinstance(rule_id, int)):
            raise TypeError('rule_id must be an int')
        if (not rule_id >= 0):
            raise ValueError('rule_id must be greater than or equal to 0')

        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'op': 'remove_delay_rule',
            'rule-id': rule_id
        }

        r = requests.post(self.url_base + '/rules', headers=headers, data=data)

        if (r.status_code / 100 == 2):
            rdict = r.json()

            if rdict['irods_response']['status_code']:
                print('Failed to remove delay rule: iRODS Status Code' + str(rdict['irods_response']['status_code']))
            else:
                print('Delay rule removed successfully')
            
            return(
                {
                    'status_code': r.status_code,
                    'data': rdict
                }
            )
        else:
            irods_err = ''
            rdict = None
            if (r.text != ''):
                rdict = r.json()
                irods_err = ': iRods Status Code' + str(rdict['irods_response'])
            print(f'Error <{r.status_code}>{irods_err}')

            return(
                {
                    'status_code': r.status_code,
                    'data': rdict
                }
            )