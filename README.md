# Dapp-Python

Full Dapp in Python

Installed Cython and web3

First of all, get web3 provider from your infura.io project

For the testing purposes, I am using OMG (OmiseGO) token

Got the abi and address of OMG token.

run the ``` truffle init ``` command to set the enviroment for our contracts

created the greeting contract with basis two functions: setGreeting and greet

Deployed the contraction using 

``` truffle deploy ```

or if it's not working, showing network is up to date then use following command.

``` truffle deploy --reset ```

Now it's time to migrate our contract. For that run the following command

``` truffle create migration greetingContract ```
