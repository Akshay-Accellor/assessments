Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-08: Ephemeral Landing Pages Compatibility', () => {
    before(async () => { await browser.url('http://www.ipsy.com/ephemeral-landing'); });
    it('Positive - Verify ephemeral landing pages can be accessed without issues', async () => {
        const page = await $('body');
        await expect(page).toBeDisplayed();
        const section = await $('.section');
        await expect(section).toBeDisplayed();
    });
    it('Negative - Verify access fails after expiration', async () => {
        await browser.url('http://www.ipsy.com/expired-ephemeral');
        const errorPage = await $('.error-404');
        await expect(errorPage).toBeDisplayed();
    });
    it('Edge - Verify compatibility after homepage update', async () => {
        await browser.url('http://www.ipsy.com/updated-ephemeral');
        const section = await $('.section');
        await expect(section).toBeDisplayed();
    });
});
