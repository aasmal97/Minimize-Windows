const { exec, execFile } = require("child_process");
const path = require("path");
const fetchWindowsJson = require("./fetchWindowsJson");
const getTypeCommand = (byType, name) => {
  let typeCommand = [];
  switch (byType) {
    case "hwnd":
      typeCommand = ["handle", name];
      break;
    case "process":
      typeCommand = ["process", name];
    case "className":
      typeCommand = ["class", name];
    default:
      return;
  }
  return typeCommand;
};
const execDirectory = path.join(__dirname, "../executables");
const execFileError = () => (err, stdout, sterr) => {
  if (err) console.error(err, "error");
  if (stdout) console.log(stdout, "message");
  if (sterr) console.error(sterr, "sterr");
};
const minimizeWindow = (byType, name) => {
  const typeCommand = getTypeCommand(byType, name);
  const command = `${execDirectory}\\nircmd.exe`;
  execFile(command, ["win", "min", ...typeCommand], execFileError);
};
const maximizeWindow = (byType, name) => {
  const typeCommand = getTypeCommand(byType, name);
  const command = `${execDirectory}\\nircmd.exe`;
  execFile(command, ["win", "max", ...typeCommand], execFileError);
};
const closeWindow = (byType, name) => {
  const typeCommand = getTypeCommand(byType, name);
  const command = `${execDirectory}\\nircmd.exe`;
  execFile(command, ["win", "close", ...typeCommand], execFileError);
};

const determineActiveWindows = async (appDataDirectory) => {
  const command = `${execDirectory}\\determineActiveWindows.exe`;
  execFile(command, ["--appDataDirectory", appDataDirectory], execFileError);
  return await fetchWindowsJson(appDataDirectory);
};
const openGui = () => {
  const command = `${path.join(__dirname, "..")}\\batFiles\\findWindow.bat`;
  exec(command, execFileError);
};

module.exports = {
  minimizeWindow,
  openGui,
  maximizeWindow,
  closeWindow,
  determineActiveWindows,
};
