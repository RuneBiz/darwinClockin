
# Run-Selenium-UI-Python-TestCase-with-Github-Action

# Why Automated Testing?

During development cycles, **manual tests** are frequently repeated for various scenarios, including source code changes, multiple operating environments, and hardware configurations.
>**Automated tests**, once developed, offer the advantage of being repeatable at no extra expense and significantly faster than manual tests. By leveraging automated software testing, the duration required to perform repetitive tests can be reduced from days to hours, resulting in time and cost savings.

>Errors can occur during repetitive manual testing tasks. Automated tests perform the same steps precisely without errors every time they are executed and never forget to record detailed results.

>Executing repetitive tasks with automated software testing gives your team time to spend on more challenging and rewarding projects.

### Sample Test Case
In sample_test_case.py,

>Function test_home_page(): will check the home page. 
To determine if the home page loading was successful, this first test will be passed.

>Function test_login_fail_with_wrong_credentials(): to verify if the login fails when using wrong credentials, we will attempt to log in with incorrect information.
If the login process fails as expected, this second test will be passed.


### Running Selenium Test Case on local
Pre-requisites:
* Chrome browser installed.
* Python 3.10 installed.

1. Clone this repo to your local.
	````bash
	git clone https://github.com/hellboyhha/Run-Selenium-UI-Python-TestCase-with-Github-Action.git
	````

2. Go to your repo downloaded directory, run this command to install python dependencies.
	````bash
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	````
3. Run sample test cases with PyTest.
	````bash
	pytest sample_test_case.py
	````
4. Sample Output from  Pytest run.
	````bash
	platform win32 -- Python 3.10.11, pytest-7.3.1, pluggy-1.0.0
	rootdir: ${your_repo_downloaded directory}
	plugins: anyio-3.6.2
	collected 2 items
	
	sample_test_case.py
	DevTools listening on ws://127.0.0.1:57649/devtools/browser/0ca78234-42c2-428e-8491-4128a28f1794.
	DevTools listening on ws://127.0.0.1:57670/devtools/browser/ecb8fb00-6b8f-4858-afa7-390654db8be8.                                                                                                                                                                                    
	                                                [100%]
	=========================================== 2 passed in 21.06s ==================================
	````
### Running Selenium Test Case with Github Action
In .github/workflows/runpytest.yml:
* This pipeline will run only on manual trigger. If you want to change trigger type, please see this documentation: https://docs.github.com/en/actions/using-workflows/triggering-a-workflow	
	````yaml
	on:
	  workflow_dispatch
	````
* This pipeline will run on windows latest machine provided by GitHub Action.
	````yaml
	runs-on: windows-latest
	````
* Set pipeline permission for publishing test results to GitHub Action Pipeline.
	````yaml
	permissions:
	  checks: write
	  pull-requests: write
	````
* Chrome browser installation using PowerShell.
	````yaml
    - name: Install Chrome Browser
      run: |
          ./chrome_installation.ps1
      shell: pwsh 
	````
* Python 3.10 and dependencies installation.
	````yaml
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
	````
* Run sample test cases and publish test results in xml format.
	````yaml
    - name: Test with pytest
      run: |
        pytest sample_test_case.py --doctest-modules --junitxml=test-results.xml
	````
* Publish test results back to GitHub Action Pipeline.
	````yaml
    - name: Publish Test Results
      uses: EnricoMi/publish-unit-test-result-action/composite@v2
      if: always()
      with:
        files: |
          test-results.xml
	````
* Trigger the pipeline manually. After the pipeline run finished, check your **test results** in pipeline summary.

	<img title="Test Results GitHub Action" alt="Alt text" src="/test_results_sample/Test Results GitHub Action.png">
