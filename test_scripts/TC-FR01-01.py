Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-01: Redesigned Homepage', () => {
    before(async () => { await browser.url('http://www.ipsy.com'); });
    it('Positive - Verify redesigned homepage is displayed as intended', async () => {
        const body = await $('body');
        await expect(body).toBeDisplayed();
        const banner = await $('.banner');
        await expect(banner).toBeDisplayed();
        const section = await $('.section');
        await expect(section).toBeDisplayed();
        const featureButton = await $('.new-feature');
        await featureButton.click();
        const featureResponse = await $('.feature-response');
        await expect(featureResponse).toBeDisplayed();
    });
    it('Negative - Verify old layout elements are not displayed', async () => {
        const oldBanner = await $('.old-banner');
        await expect(oldBanner).not.toBeDisplayed();
    });
    it('Edge - Verify homepage displays correctly on minimal viewport', async () => {
        await browser.setWindowSize(320, 480);
        const banner = await $('.banner');
        await expect(banner).toBeDisplayed();
        const section = await $('.section');
        await expect(section).toBeDisplayed();
    });
});
