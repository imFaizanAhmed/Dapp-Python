const Migrations = artifacts.require("Migrations");
const Greeting = artifacts.require("Greeter");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(Greeting);
};
