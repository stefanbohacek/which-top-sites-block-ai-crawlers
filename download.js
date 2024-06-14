import fs from "fs";

const downloadRobotsTxt = async (domain, filePath) => {
  console.log(`downloading robots.txt from ${domain}...`);
  const resp = await fetch(`https://${domain}/robots.txt`);
  const respText = await resp.text();
  // console.log(respText);
  fs.writeFileSync(filePath, await respText, "utf8");
  return respText;
};

const domains = fs.readFileSync(`./domains.txt`, "utf-8").split("\r\n");
console.log(domains);

for (const domain of domains) {
  const filePath = `./robots/${domain}.txt`;
  let respText;

  try {
    if (!fs.existsSync(filePath)) {
      respText = await downloadRobotsTxt(domain, filePath);
    } else {
      console.log(`robots.txt from ${domain} already downloaded`);
    }
  } catch (error) {
    console.log("error", domain, error);
  }
}
