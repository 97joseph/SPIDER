"use strict";

const fs = require("fs");
const util = require("util");
const axios = require("axios");
const cheerio = require("cheerio");
const FormData = require("form-data");

const baseURL = "https://cryptwerk.com";
const startURL = "https://cryptwerk.com/companies/shops/";

async function delay() {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, 2000 - Math.random() * 1000);
  });
}

async function getMainCategories() {
  console.log("MAIN CATEGORIES:", startURL);
  const { data } = await axios({
    url: startURL,
    method: "get",
  });
  const $ = cheerio.load(data);
  const mainCategories = [];
  $("select[name='categories'] option.font-weight-bold").each((_, e) => {
    const path = $(e).attr("data-url");
    const id = $(e).attr("value");
    mainCategories.push({ path, id });
  });
  return mainCategories;
}

async function getCompaniesLinksFromXHR(params) {
  console.log("LIST:", params);
  const form = new FormData();
  Object.keys(params).forEach((key) => form.append(key, params[key]));
  const { data } = await axios({
    url: "https://cryptwerk.com/ajax/companies/",
    method: "post",
    data: form,
    headers: form.getHeaders(),
  });
  const $ = cheerio.load(data.html);
  const companiesLinks = [];
  $("a[href^='/company/']").each((_, e) => {
    const link = `${baseURL}${$(e).attr("href")}`;
    if (companiesLinks.indexOf(link) === -1) companiesLinks.push(link);
  });
  return { companiesLinks, more: data.more };
}

async function getCompanyDetails(link) {
  console.log("DETAILS:", link);
  const { data } = await axios({
    url: link,
    method: "get",
  });
  const $ = cheerio.load(data);
  const service = {};
  service.name = $("h1[itemprop='name']").first().text();
  service.cryptocurrencies = $("a[title$='accepted here']")
    .map((_, e) => {
      let xs = $(e).attr("href").split("/");
      return xs.length > 2 ? xs[2] : "";
    })
    .get()
    .filter((x) => x);
  service.description = $("div.company-description").text();
  service.image = $("div.company-header img").first().attr("src");
  service.image = `${baseURL}${service.image}`;
  service.tags = $("div.categories-list > a")
    .map((_, e) => $(e).text())
    .get();
  const coordsEl = $("div.addresses div.company-map").first();
  if (coordsEl) {
    service.latLong = `${coordsEl.attr("data-lat")},${coordsEl.attr(
      "data-lng"
    )}`;
    service.address = coordsEl.attr("data-address");
  }
  service.socials = {};
  $("div.addresses div.links a").each((_, e) => {
    const key = $(e).attr("class");
    const val = $(e).attr("href");
    if (key && val.length > 1) service.socials[key] = val;
  });
  $("div.company-filters div.item").each((_, item) => {
    const field = $(item).find("span").first().text().trim(); /// I am here
    if (field === "Payment gateway") {
      service.paymentGateways = [];
      $(item)
        .find("div.tags-list > span")
        .each((_, e) => {
          service.paymentGateways.push($(e).text().trim());
        });
    } else if (field === "Fiat payments") {
      service.fiatPaymentModes = [];
      $(item)
        .find("div.tags-list > span")
        .each((_, e) => {
          service.fiatPaymentModes.push($(e).text().trim());
        });
    }
  });
  return service;
}

async function saveCompany(details) {
  return util.promisify(fs.writeFile)(
    "services.json",
    JSON.stringify(details) + ",",
    { flag: "a" }
  );
}

async function main() {
  const categoryLinks = await getMainCategories();
  await delay();
  for (let link of categoryLinks) {
    const params = {
      page: 1,
      per_page: 50,
      q: "",
      categories: link.id,
    };
    let more = true,
      companiesLinks;
    while (more === true) {
      const data = await getCompaniesLinksFromXHR(params);
      params.page += 1;
      more = data.more;
      companiesLinks = data.companiesLinks;
      await delay();
      for (let companyLink of companiesLinks) {
        const companyDetails = await getCompanyDetails(companyLink);
        await Promise.all([saveCompany(companyDetails), delay()]);
      }
    }
  }
}

main();
